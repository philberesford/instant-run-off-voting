import instant_run_off

candidates = ["Sunday, 7pm until 9pm (In Person)",
    "Sunday, 7pm until 9pm (Zoom)",
    "Alternating Tuesday/Wednesday 7pm until 9pm (In Person)",
    "Alternating Tuesday/Wednesday 7pm until 9pm (Zoom)",
    "Friday 6pm until 8pm (In Person)",
    "Friday 6pm until 8pm (Zoom)",
    "Saturday 11am until 1pm (In Person)",
    "Saturday 11am until 1pm (Zoom)"
]

votes = ["8,7,1,2,6,5,3,4",
    "5,6,1,2,3,4,7,8",
    "5,6,1,2,7,8,3,4",
    "2,4,3,5,8,7,1,6",
    "3,4,5,2,6,1,8,7",
    "2,1,6,5,4,3,8,7",
    "2,1,7,8,6,5,3,4",
    "6,5,1,2,4,3,7,8",
    "3,4,1,2,6,5,7,8",
    "4,3,2,1,8,5,6,7",
    "2,1,4,3,8,7,5,6",
    "1,2,3,4,5,6,7,8",
]

result = instant_run_off.get_result(candidates, votes)
print(result)