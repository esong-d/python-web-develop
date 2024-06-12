import { createRouter, createWebHistory} from "vue-router"
import routes from "./routes"

const router = createRouter({
    routes,
    history: createWebHistory()  //路由不会带#号
    // history: createWebHashHistory()   //路由会带#号
})

export default router