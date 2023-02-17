<template>
    <div v-if="order.hasOwnProperty('order_id')">
        <div class="item_container">
            <h1>Order No.: {{ order.order_id }}</h1>
                <h2 v-for="item in order.items" :key="item.id">
                    <hr/>
                    <h2>Product: {{ item.name }}</h2>
                    <ul>
                        <li>Price: {{ item.price }} {{ item.currency }}</li>
                        <li>Region: {{ item.region }}</li>
                        <li>Description: {{ item.description }}</li>
                    </ul>
                </h2>
        </div>  
        <hr/>
        <div class="button_container">
            <button class="button is-primary" @click="purchaseOrder()">Purchase!</button>
        </div>
    </div>
    <div v-else>
        <h1>{{ order.error }}</h1>
    </div>
</template>

/* Scripts */

<script>
    const API_URL = "http://localhost:8000/api/"
    export default {
        data() {
            return {
                order: ""
            }
        },
        methods: {
            
            async getData() {
                const orderId = this.$route.params.orderId
                try {
                    const response = await this.$axios.get(
                        API_URL + "shop/order/" + orderId /* Pass order_id from url */
                    );
                    this.order = response.data;
                    
                } catch (error) {
                    this.order = {"error": "Order doesn't exist"}
                    console.log(error);
                }
            },

            async purchaseOrder() {
                const orderId = this.$route.params.orderId
                try {
                    const response = await this.$axios.get(
                        API_URL + "create_checkout_session",
                        {params: { order_id: orderId } }
                    );
                
                    window.location.replace(response.data.checkout_session_url).catch(e => {console.log(e)})

                } catch (error) {
                    console.log(error)
                }
            },
        },
     /* Вызываем метод каждый раз при загрузке страницы */
     created() {
            this.getData();
        }
    }
</script>


/* Styles */
<style>
body {
    background-color: white;
}

.button_container .button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition-duration: 0.2s;
  
}

.button_container .button:hover {
  background-color: #20570f; /* Green */
  color: white;
}
</style>