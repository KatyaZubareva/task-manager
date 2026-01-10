import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/pages/Home.vue'
import Tasks from '@/pages/Tasks.vue'
import NotFound from '@/pages/NotFound.vue'  
import Register from '@/pages/Register.vue'
import Login from '@/pages/Login.vue'
import Profile from '@/pages/Profile.vue'
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
      path: '/profile',
      name: 'Profile',
      component: Profile
    },

    {
      path: '/subscription',
      name: 'Subscription',
      component: Subscription
    }

  ],
})

export default router
