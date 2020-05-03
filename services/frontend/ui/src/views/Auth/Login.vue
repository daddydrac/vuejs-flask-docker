<template>
    <v-content>
        <v-container
                class="fill-height"
                fluid
        >
            <v-row
                    align="center"
                    justify="center"
            >
                <v-col
                        cols="12"
                        md="4"
                        sm="8"
                >
                    <v-card class="elevation-12">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>Login form</v-toolbar-title>
                            <v-spacer/>

                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-text-field
                                        label="Login"
                                        name="login"
                                        prepend-icon="person"
                                        type="text"
                                />

                                <v-text-field
                                        id="password"
                                        label="Password"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                />
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer/>
                            <v-btn color="primary">Login</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
</template>

<script>
    export default {
        name: "Login"
    }
</script>

<style scoped>

</style>
