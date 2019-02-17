<template>
  <div class="page-style">
    <!-- Title -->
    <div class="font-weight-medium display-3">Survey Results</div>

    <!-- Display things in a grid -->
    <div class="page-grid">
      <!-- Raw numbers overview -->
      <div class="numbers-overview">
        <div class="font-weight-light headline">{{postersCount}} {{posterMsg}}</div>
        <div class="font-weight-light headline">{{usersCount}} {{usersMsg}}</div>
        <div class="font-weight-light headline"><span class="">{{targetMsg}}</span> : {{targetEmotion}}</div>
      </div>


      <div class="avg-emotions"> <!-- Average emotions graph -->
        <avg-emot class="graph-style"/>
        <v-combobox label="Select Emotions" class="graph-style"
          v-model="chosenEmotions" :items="possibleEmotions"
          multiple chips/>
      </div>
    </div>
  </div>
</template>

<script>
import AvgEmot from '../components/GAverageEmotion';

export default {
  components: { AvgEmot },
  data() {
    return {
      emotions: {
        'Anger': {key: 'anger', color: '#ffffff'},
        'Contempt': {key: 'contempt', color: '#ffffff'},
        'Disgust': {key: 'disgust', color: '#ffffff'},
        'Fear': {key: 'fear', color: '#ffffff'},
        'Happiness': {key: 'happiness', color: '#ffffff'},
        'Neutral': {key: 'neutral', color: '#ffffff'},
        'Sadness': {key: 'sadness', color: '#ffffff'},
        'Surprise': {key: 'surprise', color: '#ffffff'},
      },
      chosenEmotions: [],
      possibleEmotions: [
        'Anger',
        'Contempt',
        'Disgust',
        'Fear',
        'Happiness',
        'Neutral',
        'Sadness',
        'Surprise'
      ],
      postersCount: 5,
      usersCount: 5,
      targetEmotion: 'Happiness'
    };
  },
  computed: {
    posterMsg() {
      return `Posters Evaluated`;
    },
    usersMsg() {
      return `Users Provided Feedback`;
    },
    targetMsg() {
      return `Target Emotion`;
    }
  }
}
</script>

<style>
.graph-style {
  max-height: 400px;
  max-width: 500px;
  margin: auto;
}
.page-style {
  text-align: center;
  margin-left: 10%;
  margin-right: 10%;
}
.page-grid {
  display: grid;
  grid-template-columns: 50% 50%;
}
.numbers-overview {
  text-align: left;
}
@media only screen and (max-width: 729px) {
  .page-style {
    text-align: center;
    margin-left: 20px;
    margin-right: 20px;
  }
  .page-grid {
    display: grid;
    grid-template-columns: 100%;
  }
  .numbers-overview {
    text-align: center;
  }
}
</style>
