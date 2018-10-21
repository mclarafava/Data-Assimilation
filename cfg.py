# limit running time [s]. The program will stop after this limit
# with the best value at that moment.
time_limit = 720

# optimisation tolerance [m][m]
tolerance = 0.02
minor_error = 9999999999999

eventData = [
   {
       'eventFolder' : '',
       'modelFile' : ''
   }
]

# add the events in ascending order
raindata = [
#Event 1
  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '9',
     'minute' : '0',
     'nivel_obs' : 0.361,
     'poi_line' : 35
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '10',
     'minute' : '0',
     'nivel_obs' : 0.345,
     'poi_line' : 39
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '11',
     'minute' : '0',
     'nivel_obs' : 0.393,
     'poi_line' : 43
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '12',
     'minute' : '0',
     'nivel_obs' : 0.487,
     'poi_line' : 47
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '13',
     'minute' : '0',
     'nivel_obs' : 0.816,
     'poi_line' : 51
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '14',
     'minute' : '0',
     'nivel_obs' : 1.130,
     'poi_line' : 55
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '15',
     'minute' : '0',
     'nivel_obs' : 3.941,
     'poi_line' : 59
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '16',
     'minute' : '0',
     'nivel_obs' : 0.8792,
     'poi_line' : 63
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '17',
     'minute' : '0',
     'nivel_obs' : 0.565,
     'poi_line' : 67
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '18',
     'minute' : '0',
     'nivel_obs' : 0.487,
     'poi_line' : 71
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '19',
     'minute' : '0',
     'nivel_obs' : 0.502,
     'poi_line' : 75
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '20',
     'minute' : '0',
     'nivel_obs' : 0.502,
     'poi_line' : 79
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '21',
     'minute' : '0',
     'nivel_obs' : 1.115,
     'poi_line' : 83
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '22',
     'minute' : '0',
     'nivel_obs' : 0.895,
     'poi_line' : 87
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '4',
     'hour' : '23',
     'minute' : '0',
     'nivel_obs' : 0.612,
     'poi_line' : 91
  },

  {
     'year' : '2013',
     'month' : '11',
     'day' : '5',
     'hour' : '0',
     'minute' : '0',
     'nivel_obs' : 0.581,
     'poi_line' : 95
  }
]
  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '1',
     #'minute' : '0',
     #'nivel_obs' : 0.502,
     #'poi_line' : 99
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '2',
     #'minute' : '0',
     #'nivel_obs' : 0.471,
     #'poi_line' : 103
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '3',
     #'minute' : '0',
     #'nivel_obs' : 0.471,
     #'poi_line' : 107
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '4',
     #'minute' : '0',
     #'nivel_obs' : 0.487,
     #'poi_line' : 111
  #}
#  ]

# #Event 4

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.3768,
     #'poi_line' : 63
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '17',
     #'minute' : '0',
     #'nivel_obs' : 0.4553,
     #'poi_line' : 67
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.6594,
     #'poi_line' : 71
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.6437,
     #'poi_line' : 75
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '20',
     #'minute' : '0',
     #'nivel_obs' : 0.5652,
     #'poi_line' : 79
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '21',
     #'minute' : '0',
     #'nivel_obs' : 0.4553,
     #'poi_line' : 83
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '22',
     #'minute' : '0',
     #'nivel_obs' : 0.4396,
     #'poi_line' : 87
 #}
#]

#Event 5

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '13',
     #'minute' : '0',
     #'nivel_obs' : 0.298,
     #'poi_line' : 51,
     #'node_id' : 'N-29',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '14',
     #'minute' : '0',
     #'nivel_obs' : 0.298,
     #'poi_line' : 55,
     #'node_id' : 'N-29',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '15',
     #'minute' : '0',
     #'nivel_obs' : 0.377,
     #'poi_line' : 59,
     #'node_id' : 'N-29',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.393,
     #'poi_line' : 63,
     #'node_id' : 'N-29',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '17',
     #'minute' : '0',
     #'nivel_obs' : 0.738,
     #'poi_line' : 67,
     #'node_id' : 'N-29',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.487,
     #'poi_line' : 71,
     #'node_id' : 'N-29',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.361,
     #'poi_line' : 75,
     #'node_id' : 'N-29',
     #'model_folder' : 'Ev4'
  #}
#]

#Event 1 N-32
#{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '9',
     #'minute' : '0',
     #'nivel_obs' : 0.2418,
     #'poi_line' : 35,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '10',
     #'minute' : '0',
     #'nivel_obs' : 0.2434,
     #'poi_line' : 39,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '11',
     #'minute' : '0',
     #'nivel_obs' : 0.7269,
     #'poi_line' : 43,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '12',
     #'minute' : '0',
     #'nivel_obs' : 0.4004,
     #'poi_line' : 47,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '13',
     #'minute' : '0',
     #'nivel_obs' : 0.6123,
     #'poi_line' : 51,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '14',
     #'minute' : '0',
     #'nivel_obs' : 1.2529,
     #'poi_line' : 55,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '15',
     #'minute' : '0',
     #'nivel_obs' : 1.8793,
     #'poi_line' : 59,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.6249,
     #'poi_line' : 63,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '17',
     #'minute' : '0',
     #'nivel_obs' : 0.6657,
     #'poi_line' : 67,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.6107,
     #'poi_line' : 71,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.6406,
     #'poi_line' : 75,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '20',
     #'minute' : '0',
     #'nivel_obs' : 0.65,
     #'poi_line' : 79,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '21',
     #'minute' : '0',
     #'nivel_obs' : 1.0833,
     #'poi_line' : 83,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '22',
     #'minute' : '0',
     #'nivel_obs' : 0.7897,
     #'poi_line' : 87,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '23',
     #'minute' : '0',
     #'nivel_obs' : 0.7238,
     #'poi_line' : 91,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '0',
     #'minute' : '0',
     #'nivel_obs' : 0.6594,
     #'poi_line' : 95,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev1'
  #}
#]

#Event 4 N-32

#{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.4506,
     #'poi_line' : 63,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '17',
     #'minute' : '0',
     #'nivel_obs' : 0.3815,
     #'poi_line' : 67,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.6123,
     #'poi_line' : 71,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.526,
     #'poi_line' : 75,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '20',
     #'minute' : '0',
     #'nivel_obs' : 0.427,
     #'poi_line' : 79,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '21',
     #'minute' : '0',
     #'nivel_obs' : 0.3595,
     #'poi_line' : 83,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '22',
     #'minute' : '0',
     #'nivel_obs' : 0.4129,
     #'poi_line' : 87,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev4'
  #}
#]

#Event 5 N-32
#{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '13',
     #'minute' : '0',
     #'nivel_obs' : 0.270,
     #'poi_line' : 51,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '14',
     #'minute' : '0',
     #'nivel_obs' : 0.269,
     #'poi_line' : 55,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '15',
     #'minute' : '0',
     #'nivel_obs' : 0.281,
     #'poi_line' : 59,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.608,
     #'poi_line' : 63,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '17',
     #'minute' : '0',
     #'nivel_obs' : 0.416,
     #'poi_line' : 67,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.339,
     #'poi_line' : 71,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev5',
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.295,
     #'poi_line' : 75,
     #'node_id' : 'N-32',
     #'model_folder' : 'Ev5'
  #}
#]

#Event 1 N-3

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '9',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 35,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '10',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 39,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '11',
     #'minute' : '0',
     #'nivel_obs' : 0.3056,
     #'poi_line' : 43,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '12',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 47,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '13',
     #'minute' : '0',
     #'nivel_obs' : 0.3213,
     #'poi_line' : 51,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '14',
     #'minute' : '0',
     #'nivel_obs' : 0.6824,
     #'poi_line' : 55,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '15',
     #'minute' : '0',
     #'nivel_obs' : 1.5459,
     #'poi_line' : 59,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.5725,
     #'poi_line' : 63,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.5568,
     #'poi_line' : 71,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.5411,
     #'poi_line' : 75,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '20',
     #'minute' : '0',
     #'nivel_obs' : 0.4626,
     #'poi_line' : 79,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '21',
     #'minute' : '0',
     #'nivel_obs' : 0.7452,
     #'poi_line' : 83,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '22',
     #'minute' : '0',
     #'nivel_obs' : 0.6196,
     #'poi_line' : 87,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '4',
     #'hour' : '23',
     #'minute' : '0',
     #'nivel_obs' : 0.494,
     #'poi_line' : 91,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '0',
     #'minute' : '0',
     #'nivel_obs' : 0.5097,
     #'poi_line' : 95,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '1',
     #'minute' : '0',
     #'nivel_obs' : 0.4626,
     #'poi_line' : 99,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '2',
     #'minute' : '0',
     #'nivel_obs' : 0.4312,
     #'poi_line' : 103,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '3',
     #'minute' : '0',
     #'nivel_obs' : 0.3841,
     #'poi_line' : 107,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '5',
     #'hour' : '4',
     #'minute' : '0',
     #'nivel_obs' : 0.337,
     #'poi_line' : 111,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev1'
  #},

#]

#Event 4 N-3

#{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.2585,
     #'poi_line' : 63,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '17',
     #'minute' : '0',
     #'nivel_obs' : 0.2271,
     #'poi_line' : 67,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.3684,
     #'poi_line' : 71,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.2742,
     #'poi_line' : 75,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '20',
     #'minute' : '0',
     #'nivel_obs' : 0.2271,
     #'poi_line' : 79,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '21',
     #'minute' : '0',
     #'nivel_obs' : 0.2585,
     #'poi_line' : 83,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev4'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '6',
     #'hour' : '22',
     #'minute' : '0',
     #'nivel_obs' : 0.2271,
     #'poi_line' : 87,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev4'
  #},
#]

#Event 5 N-3
#{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '13',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 51,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '14',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 55,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '15',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 59,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '16',
     #'minute' : '0',
     #'nivel_obs' : 0.384,
     #'poi_line' : 63,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '17',
     #'minute' : '0',
     #'nivel_obs' : 0.211,
     #'poi_line' : 67,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '18',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 71,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev5'
  #},

  #{
     #'year' : '2013',
     #'month' : '11',
     #'day' : '8',
     #'hour' : '19',
     #'minute' : '0',
     #'nivel_obs' : 0.18,
     #'poi_line' : 75,
     #'node_id' : 'N-3',
     #'model_folder' : 'Ev5'
  #}
#]

inf_lim = 0.4
sup_lim = 1.6

info_node = 'N-29'

# regionalizated? nodes
result_nodes = ['N-29', 'N-3', 'N-32']

# set this flag to False if you want to update forward rainfall
skip_forward = True

# model directory
model_dir = 'model'

input_dir = 'input_rainfall'

# swmm file
swmm_filename = 'partial.inp'

# observed data spreadsheet
spreadsheet_name = 'dados.xlsx'

originals = [
              'c1.DAT',
              'c2.DAT',
              'c3.DAT',
              'c4.DAT',
              'c5.DAT',
              'c6.DAT',
              'c7.DAT',
              'c8.DAT',
              'c9.DAT',
              'c10.DAT',
              'c11.DAT',
              'c12.DAT',
              'c13.DAT',
              'c14.DAT',
              'c15.DAT'
            ]


outputs_forward = [
              'c1f.DAT',
              'c2f.DAT',
              'c3f.DAT',
              'c4f.DAT',
              'c5f.DAT',
              'c6f.DAT',
              'c7f.DAT',
              'c8f.DAT',
              'c9f.DAT',
              'c10f.DAT',
              'c11f.DAT',
              'c12f.DAT',
              'c13f.DAT',
              'c14f.DAT',
              'c15f.DAT'
            ]

outputs = [
            'c1.DAT',
            'c2.DAT',
            'c3.DAT',
            'c4.DAT',
            'c5.DAT',
            'c6.DAT',
            'c7.DAT',
            'c8.DAT',
            'c9.DAT',
            'c10.DAT',
            'c11.DAT',
            'c12.DAT',
            'c13.DAT',
            'c14.DAT',
            'c15.DAT'
           ]

# horizonte de influencia do DA
intervalHour = 2.1

# tamanho do intervalo dos dados de chuva em minutos
timeStep = 5

# number of data
ndata = int(60 / timeStep * intervalHour)

ngauges = len(originals)

# posicao das colunas dos arquivos de dados de chuva
yearc  = 1
monthc = 2
dayc   = 3
hourc  = 4
minc   = 5
rainc  = 6

global_k = None
last_mse = 9999999999999999
start_time = None
start_step_time = None
best_matrix = None
factor_matrix = None

gyear = None
gmonth = None
gday = None
ghour = None
gminute = None
gnivel_obs = None
gpoi_line = None
gdir_name = None
