<template>
    <h1>User list</h1>
    <div>
        <form>
            <label for="page">page</label>
            <input type="text" id="page" v-model="page">
            <input type="submit" @click.prevent="getData" value="查询">
        </form>
    </div>
    <div>
        <table border="1">
            <tr>
                <th>id</th>
                <th>name</th>
                <th>email</th>
            </tr>
            <tr v-for="(item, index) in data" :key="index">
                <td>{{ item.id }}</td>
                <td>{{ item.username }}</td>
                <td>{{ item.email }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
import Axios from 'axios'

export default {
    name: "UserView",
    components: {

    },
    data() {
        return {
            page: 1,
            pageSize: 10,
            data: []
        }

    },
    methods: {
        getData() {
            const params = {
                pageNum: this.page,
                pageSize: this.pageSize
            }
            Axios.post(
                'http://127.0.0.1:9090/user/query',
                params
            ).then(
                response => {

                    this.data = response.data.data
                    console.log('请求成功', response.data)
                    console.log(this.data)
                },
                error => {
                    console.log('请求失败', error.message)
                }
            )
        }
    }
}
</script>

<style>
</style>