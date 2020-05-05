<template>
    <div>
        <v-data-table
                :headers="headers"
                :items="users"
                class="elevation-1"
                sort-by="email"
        >
            <template v-slot:top>
                <v-toolbar color="white" flat>
                    <v-toolbar-title>My CRUD</v-toolbar-title>
                    <v-divider
                            class="mx-4"
                            inset
                            vertical
                    ></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog max-width="500px" v-model="dialog">
                        <template v-slot:activator="{ on }">
                            <v-btn class="mb-2" color="primary" dark v-on="on">New User</v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="headline">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12" md="12" sm="12">
                                            <v-text-field label="Username" v-model="editedItem.username"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" md="12" sm="12">
                                            <v-text-field label="Email" v-model="editedItem.email"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" md="12" sm="12">
                                            <v-text-field label="Password" v-model="editedItem.password"></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn @click="close" color="blue darken-1" text>Cancel</v-btn>
                                <v-btn @click="save" color="blue darken-1" text>Save</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-toolbar>
            </template>
            <template v-slot:item.actions="{ item }">
                <v-icon
                        @click="editItem(item)"
                        class="mr-2"
                        small
                >
                    mdi-pencil
                </v-icon>
                <v-icon
                        @click="deleteItem(item)"
                        small
                >
                    mdi-delete
                </v-icon>
            </template>
            <template v-slot:no-data>
                <v-btn @click="initialize" color="primary">Reset</v-btn>
            </template>
        </v-data-table>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "UserList",
        data: () => ({
            dialog: false,
            headers: [
                {
                    text: 'Name',
                    align: 'start',
                    sortable: false,
                    value: 'username',
                },
                {text: 'Email', value: 'email'},
                {text: 'Actions', value: 'actions', sortable: false},
            ],
            users: [],
            editedIndex: -1,
            editedItem: {
                username: '',
                email: '',
                password:''
            },
            defaultItem: {
                username: '',
                email: '',
                password:''
            },
        }),

        computed: {
            formTitle() {
                return this.editedIndex === -1 ? 'New User' : 'Edit User'
            },
        },

        watch: {
            dialog(val) {
                val || this.close()
            },
        },

        created() {
            this.initialize()
        },

        methods: {
            initialize() {
                axios({ url: process.env.VUE_APP_API_URL + '/users', method: 'GET' }).then((resp) => {
                        this.users=resp.data
                })
            },

            editItem(item) {
                this.editedIndex = this.users.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            deleteItem(item) {
                var deletedIndex = this.users.indexOf(item)
                deletedIndex = Object.assign({}, item)
                confirm('Are you sure you want to delete this item?') &&  axios({ url: process.env.VUE_APP_API_URL + '/users/'+deletedIndex.id, method: 'Delete' })
                    .then(resp => {
                        console.log(resp.data.message)
                        this.initialize()
                    })
                    .catch(err => {
                        console.log(err)
                    })
            },

            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },

            save() {
                if (this.editedIndex > -1) {
                    axios({ url: process.env.VUE_APP_API_URL + '/users/'+this.editedItem.id, data: this.editedItem, method: 'PUT' })
                        .then(resp => {
                            console.log(resp.data.message)
                            this.initialize()
                        })
                        .catch(err => {
                            console.log(err)
                        })
                    // Object.assign(this.users[this.editedIndex], this.editedItem)
                } else {
                    let userData= {
                        "email": this.editedItem.email,
                        "username": this.editedItem.username,
                        "password":this.editedItem.password
                    }
                    axios({ url: process.env.VUE_APP_API_URL + '/users', data: userData, method: 'POST' })
                        .then(resp => {
                            console.log(resp.data.message)
                            this.initialize()
                        })
                        .catch(err => {
                            console.log(err)
                        })
                }
                this.close()
            },
        },
    }
</script>

<style scoped>

</style>
