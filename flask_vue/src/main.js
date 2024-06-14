import { createApp } from 'vue'
import App from './App.vue'
import router from '../router'
import Axios from 'axios'

Axios.defaults.headers.post['Content-Type'] = 'application/json'


createApp(App)
.use(router)
.mount('#app')
