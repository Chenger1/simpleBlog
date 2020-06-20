import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/home_page'
import userRegistration from '@/components/user/regist_form'

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
    }
  ]
})
