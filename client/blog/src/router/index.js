import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/home_page'
import userRegistration from '@/components/user/regist_form'
import userLogin from '@/components/user/user_login'
import userProfile from '@/components/user/userProfile'
import createPost from '@/components/post/create_post'

Vue.use(Router)

const router =  new Router({
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
      component: createPost,
      meta: {requiresAuth:true}
    }
  ]
})
//NavigationGuard
router.beforeEach((to, from, next)=>{
  const loggedIn = localStorage.getItem('user')

  if (to.matched.some(record => record.meta.requiresAuth)){
    if(!loggedIn){
      next('/')
    }else {
      next()
    }
  } else{
    next()
  }
})
export default router