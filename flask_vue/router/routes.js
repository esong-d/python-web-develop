
const HomeView = () => import('../views/HomeView.vue')
const LoginView = () => import('../views/LoginView.vue')
const UserView = () => import('../views/UserView.vue')
const ProductView = () => import('../views/ProductView.vue')

const routes = [
    {
        path: '/',
        component: HomeView
    },
    {
        path: '/login',
        component: LoginView
    },
    {
        path: '/user',
        component: UserView
    },
    {
        path: '/product',
        component: ProductView
    }

]

export default routes