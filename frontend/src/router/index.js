import Vue from 'vue'
import Router from 'vue-router'

import HelloWorld from '@/components/HelloWorld'
import Item from '@/components/Item'
import Order from '@/components/Order'

import Success from '@/components/Success'
import Cancelled from '@/components/Cancelled'


Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/vue-hello',
      name: 'HelloWorld',
      component: HelloWorld,
    },
  
    {
      path: '/shop/item/:itemId',
      name: 'Item',
      component: Item
    },

    {
      path: '/shop/order/:orderId',
      name: 'Order',
      component: Order
    },

    {
      path: '/success',
      name: 'Success',
      component: Success
    },

    {
      path: '/cancelled',
      name: 'Cancelled',
      component: Cancelled
    }

  ]
})
