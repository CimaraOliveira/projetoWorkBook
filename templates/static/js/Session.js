class Session{
    static create(name, obj){
        this.remove(name)
        localStorage.setItem(name, JSON.stringify(obj))
    }

    static get(name){
        return JSON.parse(JSON.stringify(localStorage.getItem(name))) || null;
    }

    static remove(name){
        const local = this.get(name)
        if (local !== null){
            localStorage.removeItem(name)
        }
    }

    static clear(){
        if (localStorage.length > 0){
            localStorage.clear()
        } 
    }
}