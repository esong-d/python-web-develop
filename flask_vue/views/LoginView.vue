<template>
    <h1>login</h1>
    <div class="login-container">
        <form action="#">
            <div>
                <label for="name">name</label>
                <input type="text" value="请输入名字" id="name" class="name">
            </div>
            <div>
                <label for="password">password</label>
                <input type="password" value="password" id="password" class="password">
            </div>
            <input type="submit" value="登录">
        </form>
    </div>
</template>

<script>
    export default {
        name: 'loginView',
        components: {
        },
        data() {
            return {
                name: '',
                password: ''
            }
        },
        methods: {
            login() {
                console.log(this.name, this.password)
            }
        }
    }
</script>