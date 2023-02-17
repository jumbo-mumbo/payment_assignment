import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import Stripe from 'stripe'

Vue.prototype.$axios = axios;
Vue.prototype.$Stripe = Stripe;
Vue.config.productionTip = false;


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
