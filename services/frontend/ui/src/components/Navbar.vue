<template>
    <nav>
        <v-app-bar :dark="this.$store.state.dark" app color="gray">

            <v-toolbar-title class="text-uppercase">
                <span class="font-weight-light">Sample  Auth </span>
                <span>Vuetify</span>
            </v-toolbar-title>
            <v-spacer>
            </v-spacer>
            <v-menu offset-y>
                <template v-slot:activator="{ on }">
                    <v-btn
                            text
                            v-on="on"
                    >
                        <v-icon left>expand_more</v-icon>
                        <span>Menu</span>
                    </v-btn>
                </template>
                <v-list flat>
                    <v-list-item :key="link.text" :to="link.route" active-class="border" router v-for="link in links">
                        <v-list-item-title>{{link.text}}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>

            <v-btn @click="logout" text>
                <span>Logout</span>
                <v-icon right>exit_to_app</v-icon>
            </v-btn>
            <v-app-bar-nav-icon  @click.stop="drawer = !drawer">

            </v-app-bar-nav-icon>
        </v-app-bar>
        <v-navigation-drawer right :dark="this.$store.state.dark" app class="gray darken-4" v-model="drawer">
            <v-list flat>
                <v-switch :label="`Dark Theme`" @change="switchColor" v-model="mode"></v-switch>
                <v-list-item :key="link.text" :to="link.route" active-class="border" router v-for="link in links">
                    <v-list-item-action>
                        <v-icon>{{link.icon}}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>{{link.text}}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
    export default {
        name: "Navbar",
        data: () => ({
            mode: true,
            drawer: true,
            links: [
                {icon: 'dashboard', text: 'Dashboard', route: '/'},
                {icon: 'verified_user', text: 'Register', route: '/register'},
                {icon: 'account_box', text: 'User List', route: '/list-user-data'},
                {icon: 'settings_applications', text: 'Control Panel', route: '/control-panel'}
            ],
        }),
        computed: {
            isLoggedIn: function () {
                return this.$store.getters.isLoggedIn
            }
        },
        methods: {
            logout: function () {
                this.$store.dispatch('logout')
                    .then(() => {
                        this.$router.push('/login')
                    })
            },
            switchColor(event) {
                this.$store.state.dark = event
            }
        },
    }
</script>

<style>
    .border {
        border-left: 4px solid cyan;
    }
</style>
