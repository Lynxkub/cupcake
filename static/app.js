
function clearInputs(){
const $flavor = $('#flavor')
const $size = $('#size')
const $rating = $('#rating')
const $image = $('#image')
$flavor.val('')
$size.val('')
$rating.val('')
$image.val('')
}

async function deleteCupcake(){
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
}


$('.delete_cupcake').click(deleteCupcake);


async function addCupcake(e){
    e.preventDefault();
    let flavor = $('#flavor').val()
    let size = $('#size').val()
    let rating = $('#rating').val()
    let image = $('#image').val()
    const cupcake = await axios.post('/', {flavor, size, rating,image})
    clearInputs();
    console.log(cupcake)
    $('cupcake_list').append(cupcake);

}



$('.addCupcake').click(addCupcake)



async function editCupcake(e){
    e.preventDefault();
    let flavor = $('#flavor').val()
    let size = $('#size').val()
    let rating = $('#rating').val()
    let image = $('#image').val()
    const id = $(this).data('id')
    const cupcake = await axios.patch(`/api/cupcakes/${id}`, {flavor, size, rating, image})
}

$('#confirm_edit').click(editCupcake)




