<script>
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  props: ['data', 'emotion'],
  mounted() {
    this.renderChart(this.avgemotion, this.options);
  },
  computed: {
    avgemotion() {
      // Loop through each poster
      
        // For each poster, find the average for the given emotion


      // Return the data structure that chartJS expects
      return {
        labels: ['A', 'B', 'C', 'D'],
        datasets: [{
          label: `Average Emotion - ${this.emotion}`,
          backgroundColor: '#81a1d1',
          data: [1, 2, 3, 4],
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
              suggestedMax: 5
            }
          }]
        },
        maintainAspectRatio: false
      }
    };
  }
}
</script>