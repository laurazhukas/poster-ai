<script>
import { Radar } from 'vue-chartjs';

export default {
  extends: Radar,
  props: [],
  mounted() {
    this.renderChart(this.avgemotion, this.options);
  },
  computed: {
    avgemotion() {
      // Loop through each poster
      
        // For each poster, find the average for the given emotion


      // Return the data structure that chartJS expects
      return {
 
        labels: ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise'],
        datasets: [{
        //   label: `User Age Demographics - ${this.age}`,
          label: 'User 1',
          data: [24, 36, 57, 93, 42, 23, 37, 12],
          backgroundColor: "rgba(0,0,0,0.5)"
        },
        {
          label: 'User 2',
          data: [45, 43, 27, 19, 65, 60, 29, 35],
          backgroundColor: "rgba(255,0,0,0.5)"
        },
        {
          label: 'User 3',
          data: [56, 69, 30, 10, 69, 60, 50, 61],
          backgroundColor: "rgba(0,0,255,0.5)"
        },]
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
  }
}
</script>