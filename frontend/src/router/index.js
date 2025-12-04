import Home from '@/pages/Home.vue'
import Tasks from '@/pages/Tasks.vue'
import NotFound from '@/pages/NotFound.vue'  
import { createRouter, createWebHistory } from 'vue-router'
import Register from '@/pages/Register.vue'
import Login from '@/pages/Login.vue'
import Subscription from '@/pages/Subscription.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },

    {
      path: '/tasks',
      name: 'Tasks',
      component: Tasks
    },

    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: NotFound
    },

    {
      path: '/register',
      name: 'Register',
      component: Register
    },

    {
      path: '/login',
      name: 'Login',
      component: Login
    },

    {
      path: '/subscription',
      name: 'Subscription',
      component: Subscription
    }

  ],
})

export default router
