<template>
  <div class="control-panel section">
    <div class="control-panel__select">
      <v-container fluid>
        <v-row align="center">
          <v-col class="d-flex">
            <v-select
              :items="pressureOptions"
              background-color="#D9E5F0"
              label="Select: Tires Pressure"
              solo
            >
              <v-icon slot="append">mdi-arrow-down-circle-outline</v-icon>
            </v-select>
            </v-col>
          </v-row>
      </v-container>
    </div>
    <div class="control-panel__wheels">
      <span class="top-left">2.2 BAR</span>
      <span class="top-right">1.9 BAR</span>
      <span class="bottom-left">2.2 BAR</span>
      <span class="bottom-right">2.2 BAR</span>
      <img src="../assets/wheel-chassis.png" class="chassis" />
      <WheelsSVG :isRightFilled="'true'" />
      <WheelsSVG :isRightFilled="'false'" />
    </div>
    <div class="control-panel__alerts">
      <v-card
        class="mx-auto"
        elevation="12"
      >
        <v-card-text>
          <div class="text">
            <v-icon>mdi-alert-circle</v-icon>Check your front right tire!
          </div>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>
    import axios from 'axios';
    import WheelsSVG from "../components/WheelsSVG";

    export default {
        name: "ControlPanel",

        components: {WheelsSVG},

        data: () => ({
            userData: [],
            pressureOptions: [1.8,1.9,2.0,2.1]
        }),

        created() {
            this.getUserData()
        },

        methods: {
            getUserData() {
                axios({ url: process.env.VUE_APP_API_URL + '/users', method: 'GET' }).then((resp) => {                        
                        this.userData = this._l.get(resp, 'data');
                })
            }
        }
    }
</script>

<style lang="scss" scoped>
  @import '../scss/main.scss';

  .control-panel {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    &__select {
      min-width: 400px;
    }    

    &__wheels {
      position: relative;
      color: $font-color;

      .chassis {
        transform: scale(1.5);
        position: absolute;
        top: 30%;
        left: 45%;
      }

      .top-left {
        position: absolute;
        top: -10px;
        left: 1%;
      }

      .top-right {
        position: absolute;
        right: 2%;
        top: -6%;
      }

      .bottom-left {
        position: absolute;
        top: 44%;
        left: 1%;
      }

      .bottom-right {
        position: absolute;
        right: 2%;
        top: 44%;
      }  
    }

    &__alerts {
      min-width: 400px;
      padding-top: 30px;

      .v-card.v-sheet.theme--light{
        background-color: $element;
      }

      .text {
        display: flex;
        align-items: center;
        justify-content: center;

        .v-icon {
          margin-right: 10px;
        }
      }
    }
  }

</style>
