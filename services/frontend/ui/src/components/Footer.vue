<template>
  <v-footer
          app
          :dark="this.$store.state.dark"
          inset
          padless

  >
    <v-card
            :elevation="10"
            class="flex"
            color="gray"
            flat
            tile
    >

      <v-card-text class="py-2  text-center">
        {{ new Date().getFullYear() }} — <strong>SAMPLE AUTH VUETIFY</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>
