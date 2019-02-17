<script>
import { Doughnut } from 'vue-chartjs';

export default {
  extends: Doughnut,
  props: ['age'],
  mounted() {
    this.renderChart(this.avgemotion, this.options);
  },
  computed: {
    avgemotion() {
      // Loop through each poster
      
        // For each poster, find the average for the given emotion


      // Return the data structure that chartJS expects
      return {
        labels: ['18-30', '30-50', '60-80', '80+'],
        datasets: [{
        //   label: `User Age Demographics - ${this.age}`,
          label: 'Test Label',
          data: [24, 36, 57, 93],
          backgroundColor: ["#FF6384",'#81a1d1', "#36A2EB", "#FFCE56"]
        },]
      }
    }
  },
  data() {
    return {
      options: {
       title: {
           display: true,
           position: "bottom",
           text: "User Age Demographics"
       },
        maintainAspectRatio: false
      }
    };
  }
}
</script>