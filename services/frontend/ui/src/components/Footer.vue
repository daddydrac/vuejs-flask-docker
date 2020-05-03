<template>
  <v-footer
          app
          dark
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

      <v-card-text class="py-2 white--text text-center">
        {{ new Date().getFullYear() }} — <strong>AAE IdeaPro</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>
