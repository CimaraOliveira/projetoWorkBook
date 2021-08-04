$("#submit_login").click(async function(){
    const button = $(this)
    button.attr('type', 'button')
    await getKey(async (res) => {
        console.log(res)
        Session.create('key', res.data)
        await Req.getJSON({uri: `${uri_api_auth_key}`, params: {key: res.data.key}, headers:{
            'Authorization': `Basic ${btoa($("#username").val()+':'+$("#password").val())}`
        }, 
        onSuccess: (res) => {
            Session.create('id', res.data)
            button.attr('type', 'submit')
            console.log(button)
           $('form').submit()
        }, onError: (d) => {
            button.attr('type', 'submit')
            $('form').submit()
        }})
    }) 
})    

async function getKey(fc){
    //get_by_username_password
    const username = $("#username").val()
    const password = $("#password").val()
    const basic = btoa(username+':'+password)
    Session.create('basic', `${basic}`)
    await Req.getJSON({uri: `${uri_api_username_password}`, params: {username: username, password: password}, headers:{
        'Authorization': `Basic ${basic}`
    }, onSuccess: fc, onError: (d) => console.log(d)})
}