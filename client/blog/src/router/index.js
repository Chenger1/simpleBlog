import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/home_page'
import userRegistration from '@/components/user/regist_form'
import userLogin from '@/components/user/user_login'
import userProfile from '@/components/user/userProfile'
import createPost from '@/components/post/create_post'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/registration',
      name: 'userRegistration',
      component: userRegistration
    },
    {
      path: '/login',
      name: 'userLogin',
      component: userLogin
    },
    {
      path: '/userProfile',
      name: 'userProfile',
      component: userProfile
    },
    {
      path: '/createPost',
      name: 'createPost',
      component: createPost
    }
  ]
})
