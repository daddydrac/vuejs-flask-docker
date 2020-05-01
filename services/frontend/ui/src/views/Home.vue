<template>
  <v-container>
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-text-field
        v-model="name"
        :counter="10"
        :rules="nameRules"
        label="Name"
        required
      ></v-text-field>

      <v-btn
        :disabled="!valid"
        color="primary"
        class="mr-4"
        @click="validate"
      >
        Validate
      </v-btn>
    </v-form>
    {{ name }}
    {{ response }}
  </v-container>
</template>

<script>
  import axios from 'axios';

  export default {
    data: () => ({
      response: null,
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
    }),

    methods: {
      validate () {
        const isValid = this.$refs.form.validate();
        // if form is valid, send AJAX request to Flask
        if (isValid) {
          axios
          .post('http://localhost:5009/name', {name: this.name})
          .then(res => { this.response = res })
          .catch(err => { console.log(err); });
        }

      },
    },
  }
</script>
