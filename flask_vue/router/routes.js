
const HomeView = () => import('../views/HomeView.vue')
const LoginView = () => import('../views/LoginView.vue')

const routes = [
    {
        path: '/home',
        RouterView: HomeView
    },
    {
        path: '/login',
        RouterView: LoginView
    },

]

export default routes