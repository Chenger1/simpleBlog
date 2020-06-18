<template>
    <div class="navbar navbar-dark bg-dark">
        <h1 class="navbar-brand">
            {{sitename}}
        </h1>
    </div> 
</template>
<script>
export default {
    name: 'my-header',
    data (){
        sitename: 'simpleBlog'
    }
}
</script>