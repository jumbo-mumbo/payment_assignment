<template>
    <div v-if="item.hasOwnProperty('name')">
        <div class="item_container">
                <h1>Product: {{ item.name }}</h1>
                    <h2><ul>
                        <li>Price: {{ item.price }} {{ item.currency }}</li>
                        <li>Region: {{ item.region }}</li>
                        <li>Description: {{ item.description }}</li>
                    </ul>
                    </h2>
            </div>
            <div class="button_container">
                <button class="button is-primary" @click="purchaseItem()">Purchase!</button>
            </div>
    </div>
    <div v-else>
        <h1>{{ item.error }}</h1>
    </div>
</template>

/*  Scripts */
<script src="https://js.stripe.com/v3"></script>
<script>
    
    const API_URL = "http://localhost:8000/api/"
    export default {
        data() {
            return {
                item: ""
            }
        },
        methods: {
            
            async getData() {
                const itemId = this.$route.params.itemId
                try {
                    const response = await this.$axios.get(
                        API_URL + "shop/item/" + itemId /* Pass item_id from url */
                    );
                    this.item = response.data;
                    
                } catch (error) {
                    this.item = {"error": "Item doesn't exist"}
                    console.log(error);
                }
            },
            
            async purchaseItem() {
                const itemId = this.$route.params.itemId
                const stripe = this.$Stripe(this.getPublicKey());
                
                try {
                    const response = await this.$axios.get(
                        API_URL + "create_checkout_session",
                        {params: { id: itemId } }
                    );
                
                    window.location.replace(response.data.checkout_session_url).catch(e => {console.log(e)})

                } catch (error) {
                    console.log(error)
                }
            },

            async getPublicKey() {
                try {
                    const publicKey = await this.$axios.get(
                        API_URL + "get_public_key"
                    )
                    return publicKey

                } catch (error) {
                    console.log(error)
                }
            }

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