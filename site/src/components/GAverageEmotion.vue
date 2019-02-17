<script>
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  props: ['data', 'emotions'],
  mounted() {
    this.renderChart(this.avgemotion, this.options);
  },
  computed: {
    avgemotion() {
      // let posterEmotions = {};
      // let posterEmotions = [];

      // One label per poster
      let labels = [];

      // The final dataset list, associated with a given emotion
      let datasets = [];

      // For each emotion, have some data
      let emotionData = {};
      for(let e of this.emotions) {
        emotionData[e] = [];
      }

      // Loop through each poster, push a dataset
      for(let poster of this.data) {
        // Set the label
        labels.push(poster.id);

        // Go through each emotion, and then each face
        for(let e of this.emotions) {
          let total = 0;

          // Add up the emotional value of all the faces
          for(let f of poster.faces) {
            total += f.faceAttributes.emotions[e];
          }

          // Average
          total = total / poster.faces.length;
          
          // Then push to emotion data
          emotionData[e].push(total);
        }
      }

      
      // Push the averaged data
      for(let e of this.emotions) {
        datasets.push({
          label: e,
          backgroundColor: this.colors[e],
          data: emotionData[e]
        });
      }

      // Return the data structure that chartJS expects
      return {
        labels: labels,
        datasets: datasets
        // datasets: [{
        //   label: `Average Emotions`,
        //   backgroundColor: '#81a1d1',
        //   data: posterEmotions,
        // },]
      }
    }
  },
  watch: {
    emotions() {
      this.renderChart(this.avgemotion, this.options);
    },
    data() {
      this.renderChart(this.avgemotion, this.options);
    },
  },
  methods: {
    
  },
  data() {
    return {
      colors: {
        anger: '#e84747',
        contempt: '#72756d',
        disgust: '#e2b844',
        fear: '#435763',
        happiness: '#40c450',
        neutral: '#bababa',
        sadness: '#3e3572',
        surprise: '#962d7d',
      },
      options: {
        scales: {
          yAxes: [{
            stacked: true,
            ticks: {
              suggestedMin: 0,
              suggestedMax: 1.0
            }
          }],
          xAxes: [{
            stacked: true,
          }]
        },
        maintainAspectRatio: false
      }
    };
  }
}
</script>