const formToJSON = elements => [].reduce.call(elements, (data, element) => {
  if (isValidElement(element)) {
    data[element.name] = element.value;
  }
  return data;
}, {});

const isValidElement = element => {
  return element.name && element.value;
};

function authenticate(form){
   const data = formToJSON($('#loginFrm').serializeArray());
    var formData = JSON.stringify(data)
    fetch("/auth", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(
        res=> {
            if (res.redirected) {
                window.location.replace(res.url)
            } else {
                return res.json()
            }
        }
    ).then(res=>{
        try {
                    $('#resp').text(res.text)
                    $('#resp').show();
                    if (res.res == 200) {
                        $('#resp').addClass('alert alert-success')
                    } else if (res.res == 400){
                        $('#resp').addClass('alert alert-danger')
                    }
                } catch (err) {
                    $('#resp').text("Server Error!")
                    console.log(err)
                    $('#resp').show();
                    $('#resp').addClass('alert alert-danger')
                }
    })

}

function register(form){

    const data = formToJSON($('#regFrm').serializeArray());
    var formData = JSON.stringify(data)
    fetch("/register", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(res => res.json()).then(res=> {
            $('#resp').text(res.text)
            $('#resp').show();
            if (res.res == 200) {

                $('#resp').addClass('alert alert-success')
            } else {
                $('#resp').addClass('alert alert-danger')
            }
        }
    )
}

$(document).ready(function(){
    $('#resp').hide();
})