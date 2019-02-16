<template>
  <v-app>
        <!-- Navigation bar -->
    <v-toolbar dense flat>
      <v-toolbar-title>Poster-AI</v-toolbar-title>
      <v-spacer/>
      <v-toolbar-side-icon class="hidden-sm-and-up" @click="drawerOpen = !drawerOpen"/>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn to="/" flat>Home</v-btn>
        <v-btn to="/updates" flat>Updates</v-btn>
        <v-btn to="/about" flat>About</v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <!-- Drawer for mobile menu -->
    <v-navigation-drawer v-model="drawerOpen" absolute temporary right>
      <v-list>
        <!-- Home Link -->
        <v-list-tile to="/">
          <v-list-tile-action> <v-icon>home</v-icon> </v-list-tile-action>
          <v-list-tile-title>Home</v-list-tile-title>
        </v-list-tile>

        <!-- Updates Link -->
        <v-list-tile to="/updates">
          <v-list-tile-action> <v-icon>description</v-icon> </v-list-tile-action>
          <v-list-tile-title>Updates</v-list-tile-title>
        </v-list-tile>

        <!-- About Link -->
        <v-list-tile to="/about">
          <v-list-tile-action> <v-icon>info</v-icon> </v-list-tile-action>
          <v-list-tile-title>About</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <!-- And finally all the way at the bottom... the actual page content :) -->
    <router-view/>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
      drawerOpen: false
    }
  }
}
</script>
