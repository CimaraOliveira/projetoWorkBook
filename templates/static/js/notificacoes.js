$(document).ready(async function () {
    const { id } = JSON.parse(Session.get('id'))
    if ($("#notificacoes").length) {
        const { key } = JSON.parse(Session.get('key'))
        const resp = await Req.getJSON({ uri: `${uri_api_notificacao_get_status}`, params: { token: key } })
        if (resp.status === 200) {
            await renderNotificacao(await resp.json())
        }
    }
});

function getBadgeSize(size) {
    document.getElementById('badge-size').innerHTML =
    `<div class="bs-component" style="position: absolute;top: 2px;right: 5px;">
        <span class="badge badge-danger" style="font-size: 10px;">${size}</span>
    </div>`
}

async function renderNotificacao(data) {
    if (Array.isArray(data)) {
        getBadgeSize(data.length)
        for (let obj of data) {
            const { notificacao, size } = obj
            //   console.log(notificacao)
            let user = null
            const resp = await Req.getJSON({ uri: `${uri_api_messages}get_by_id/`, params: { id: notificacao.mensagemRecebida } })
            if (resp.status === 200) {
                const mensagem = await resp.json() 
                user = await getUser(mensagem.remetente) 
            
                const spanBadge = new Tag({ tagName: 'span', value: size, attrs: { class: 'badge badge-danger', style: 'font-size: 10px;' } })
                const divComponent = new Tag({ tagName: 'div', children: [spanBadge], attrs: { class: 'bs-component', style: 'position: absolute; bottom: 21px; right: 0px;' } })
                const divApp = new Tag({ tagName: 'div', value: `${user ? user.username : user} ${notificacao.texto}`, attrs: { class: 'app-notification__message', style: 'display: flex; justify-content: center; align-items: center;' } })
                //const iCircle = new Tag({ tagName: 'i', children: [], attrs: { class: 'fa fa-circle fa-stack-2x text-primary' } })
                //const iEnvelope = new Tag({ tagName: 'i', children: [], attrs: { class: 'fa fa-envelope fa-stack-1x fa-inverse' } })
                const imagem = new Tag({ tagName: 'img', attrs: { src: `${user && user.imagem ? user.imagem : 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png'}`, style: 'max-width: 30px; height: auto' } })
                const spanStack = new Tag({ tagName: 'span', children: [divComponent, imagem], attrs: { class: 'fa-stack fa-lg' } })
                const spanApp = new Tag({ tagName: 'span', children: [spanStack], attrs: { class: 'app-notification__icon', style: " display: flex; justify-content: center; align-items: flex-end;" } })
                const a = new Tag({ tagName: 'a', children: [spanApp, divApp], attrs: { class: 'app-notification__item', onclick: `save_id_perfil(${mensagem.remetente}, ${notificacao.id})`, href: '#'} })
                const li = new Tag({ tagName: 'li', children: [a] })
                const liView = new TagView(li)
                View.append(liView.element, document.getElementById('notificacoes'))
            }
        }
    }
}