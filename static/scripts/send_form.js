function checkLightSwitch(){
    let lightSwitch = document.getElementById('light-switch');

    $.ajax({
            url:'/getValueFromLightSwitch',
            type:'POST',
            data: {'status': lightSwitch.checked}
        })
}