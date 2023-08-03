// imports 
const express = require('express')
const app = express()
const port = 3000 

// Static files 
app.use(express.static('public'))
app.use('/css', express/static(_dirname + 'public/css'))
app.use('/js', express/static(_dirname + 'public/js'))
app.use('/img', express/static(_dirname + 'public/img'))

app.get('', (req, res) => {
    res.sendFile(__dirname + '/pages/index.html')
})



// List on port 3000  
app.listen(port, () => console.info('Listening on port ${port}'))

