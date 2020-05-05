<template>
    <v-app>
        <Navbar v-if="this.$store.getters.isLoggedIn"/>
        <v-content class="ma-4">
            <router-view></router-view>
        </v-content>
        <Footer v-if="this.$store.getters.isLoggedIn"/>
    </v-app>
</template>
<script>
    import Navbar from "./components/Navbar";
    import Footer from "./components/Footer";

    export default {
        name: 'App',
        components: {Navbar, Footer},
        created: function () {
            // this.$http.interceptors.response.use(undefined, function (err) {
            //     // return new Promise(function (resolve, reject) {
            //     //     if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
            //     //         this.$store.dispatch(logout)
            //     //     }
            //     //     throw err;
            //     // });
            // });
        }
    }
</script>
