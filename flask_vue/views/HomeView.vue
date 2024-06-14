<template>
    <div class="home">
        <h1>home</h1>
        <div>
            <router-link to="/login">login</router-link> |
            <router-link to="/user">user</router-link> |
            <router-link to="/product">product</router-link>
        </div>
    </div>
    <router-view></router-view>
    
</template>

<script>

export default {
    name: 'homeView', 
    components: {
    }
}
</script>
<style>
.home {
    margin-top: 50px;
}
</style>