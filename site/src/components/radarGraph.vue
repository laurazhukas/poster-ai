<script>
import { Radar } from 'vue-chartjs';

export default {
  extends: Radar,
  props: ['data', 'emotions'],
  mounted() {
    this.renderChart(this.avgemotion, this.options);
  },
  computed: {
    avgemotion() {
      // One dataset per face, make it simple
      let datasets = [];
      let i = 0; 
      let max = this.data.length;
      console.log(this.data);
      for(let user of this.data) {
        i += 1;
        datasets.push({
          label: `User #${i}`,
          data: [
            parseFloat(user.anger),
            parseFloat(user.contempt),
            parseFloat(user.disgust), 
            parseFloat(user.fear),
            parseFloat(user.happiness),
            parseFloat(user.neutral),
            parseFloat(user.sadness),
            parseFloat(user.surprise)
          ],
          // backgroundColor: `rgb(${i / max}, ${(max - i) / max}, 0.3)`
          backgroundColor: '#'+Math.random().toString(16).substr(-6)
          // backgroundColor: "#ffffff"
          // backgroundColor: 'rgb(0.5, 0.5, 0.5)'
        })
      }
      
      // Return the data structure that chartJS expects
      return {


        labels: this.emotions,
        datasets: datasets

 
        // labels: ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise'],
        // datasets: [{
        // //   label: `User Age Demographics - ${this.age}`,
        //   label: 'User 1',
        //   data: [24, 36, 57, 93, 42, 23, 37, 12],
        //   backgroundColor: "rgba(0,0,0,0.5)"
        // },
        // {
        //   label: 'User 2',
        //   data: [45, 43, 27, 19, 65, 60, 29, 35],
        //   backgroundColor: "rgba(255,0,0,0.5)"
        // },
        // {
        //   label: 'User 3',
        //   data: [56, 69, 30, 10, 69, 60, 50, 61],
        //   backgroundColor: "rgba(0,0,255,0.5)"
        // },]
      }
    }
  },
  data() {
    return {
      options: {
        scales: {
          yAxes: [{
            ticks: {
              suggestedMin: 0,
              suggestedMax: 1.0
            }
          }],
        },
        maintainAspectRatio: false
      }
    };
  },
  watch: {
    emotions() {
      this.renderChart(this.avgemotion, this.options);
    },
    data() {
      this.renderChart(this.avgemotion, this.options);
    },
  }
}
</script>