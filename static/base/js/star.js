const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')
const confirmBox = document.getElementById('confirm-box')

const form = document.querySelector('.rate-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form.children
    for(let i = 0; i < children.length; i++){
        if(i <= size){
            children[i].classList.add('checked')
        }else {
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
            handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'fourth': {
            handleStarSelect(4)
            return
        }
        case 'fifth': {
            handleStarSelect(5)
            return
        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if( stringValue === 'first'){
        numericValue = 1
    }
    else if( stringValue === 'second'){
        numericValue = 2
    }
    else if( stringValue === 'third'){
        numericValue = 3
    }
    else if( stringValue === 'fourth'){
        numericValue = 4
    }
    else if( stringValue === 'fifth'){
        numericValue = 5
    }
    else {
        numericValue = 0
    }
    return numericValue 
}

if(one){
    const arr = [one, two, three, four, five]

    arr.forEach(item => item.addEventListener('mouseover',(event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item => item.addEventListener('click',(event)=>{
        val = event.target.id
        console.log(val)
        const val_num = getNumericValue(val)
        console.log(val_num)

        $.ajax({
            type: 'GET',
            data: {
                'csrfmiddlearetoken': csrf[0].value,
                'val': val_num,
            }, 
            success: function(response){
                console.log(response)
                confirmBox.innerHTML = `<div class="alert alert-success"><i class="fas fa-check-circle"></i> Ha calificado satisfactoriamente con ${val_num} estrellas 
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button></div>`
            }, 
            error: function(error){
                console.log(error)
            }
        })
    }))
}
