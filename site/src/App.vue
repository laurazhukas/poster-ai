<template>
  <v-app>

    <!-- Navigation bar -->
    <v-toolbar dense flat dark color=black>
      <v-toolbar-title>Poster AI</v-toolbar-title>
      <v-spacer/>
      <v-toolbar-side-icon class="hidden-sm-and-up" @click="drawerOpen = !drawerOpen"/>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn to="/" flat>Home</v-btn>
        <v-btn to="/about" flat>About</v-btn>
        <v-btn to="/commercial" flat>Commercial Opportunities</v-btn>
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

        <!-- About Link -->
        <v-list-tile to="/about">
          <v-list-tile-action> <v-icon>info</v-icon> </v-list-tile-action>
          <v-list-tile-title>About</v-list-tile-title>
        </v-list-tile>

        <!-- Commercial Opportunities Link -->
        <v-list-tile to="/commercial">
          <v-list-tile-action> <v-icon>opportunities</v-icon> </v-list-tile-action>
          <v-list-tile-title>Commercial Opportunities</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <!-- Page content -->
    <router-view/>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  components: {
    
  },
  data () {
    return {
      drawerOpen: false
    }
  }
}
</script>
