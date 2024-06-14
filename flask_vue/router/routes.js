
const HomeView = () => import('../views/HomeView.vue')
const LoginView = () => import('../views/LoginView.vue')

const routes = [
    {
        path: '/',
        component: HomeView
    },
    {
        path: '/login',
        component: LoginView
    },

]

export default routes