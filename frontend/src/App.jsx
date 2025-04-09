import { useState } from 'react'

// Checker added to make colorful balls related to the number of balls in the array so I will check the values and asign a color to each ball
const checkColor = (value) => {
  if (value < 10) {
    return 'bg-red-500'
  } else if (value < 20) {
    return 'bg-yellow-500'
  } else if (value < 30) {
    return 'bg-green-500'
  } else if (value < 40) {
    return 'bg-blue-500'
  } else {
    return 'bg-purple-500'
  }
}

// I created a ball component to map the numbers to the balls
const Ball = ({ value }) => {
  return (
    <div className={`w-10 h-10 rounded-full ${checkColor(value)} flex items-center justify-center text-white`}>
      {value}
    </div>
  )
}

export default function App() {
  // I used to state method in React to create a state for the balls and the bonus number
  const [balls, setBalls] = useState([])
  const [bonus, setBonus] = useState(null)

  const fetchNumbers = async () => {
    // I used the fetch method to get the data from the backend
    // As you remember it returns an array of numbers and a bonus number
    const respond = await fetch('http://localhost:8000/backend/generate_numbers')
    const data = await respond.json()
    setBalls(data.numbers) 
    setBonus(data.bonus_ball)
  }

  // Tailwind allow us to give styles with just a class name
  // Documentation : https://tailwindcss.com/docs
  
  return (
   <div className='min-h-screen flex flex-col items-center justify-center bg-gray-100 p-6' >
      <h1 className='text-2xl font-bold mb-4'>Random Number Generator</h1>
      <div className='flex gap-4 mb-4'>
         {/* I used the map method to map the balls to the ball component and I used the number as a key value too because they are unique anyway */}
        {balls.map((number) => (
          <Ball key={number} value={number} />
        ))}
      </div>
      {/* I used conditional rendering expression so if bonus value exist it will show up */}
      {bonus && (
        <div className="flex items-center gap-2 mb-4">
          <span className="font-semibold">Bonus:</span>
          <Ball value={bonus} />
        </div>
      )}
      {/* I used the fetch method to get the data from the backend on click to button */}
      <button onClick={fetchNumbers} className='bg-green-500 text-white px-4 py-2 rounded shadow hover:bg-indigo-700 transition mb-4'>
        Start Lottery
      </button>
   </div>
  )
}

// IN FUTURE 
// I can add a aanimation to the balls when they are generated
// I can add a loader to the button when it is clicked
// I can add a sound when the button is clicked
// I can add a sound when the balls are generated
// I can add routing system and diffent pages like Login, Register, Lottery History, etc
// And I can containerize the app with Docker and move to Kubernetes or deploy in AWS EC2 

