class Session{
    static create(name, obj){
        localStorage.setItem(name, JSON.stringify(obj))
    }

    static async get(name){
        return await JSON.parse(JSON.stringify(localStorage.getItem(name))) || null;
    }

    static async remove(name){
        const local = await this.get(name)
        if (local !== null){
            localStorage.removeItem(name)
        }
    }

    static async clear(){
        if (localStorage.length > 0){
            localStorage.clear()
        } 
    }
}