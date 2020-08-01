<template>
    <div>
        <svg width="400" height="80" viewBox="0 0 680 100">
            <polyline points="5,5 100,5 140,60 190,60" style="fill:none;stroke:#c8cccf;stroke-width:4" />

            <rect x="200" y="20" rx="15" ry="15" width="50" height="80" style="fill:#FFFFFF;stroke:#DFE3E6;stroke-width:5;opacity:0.8" />
  
            <rect x="420" y="20" rx="15" ry="15" width="50" height="80" :style="getRectStyle" />
  
            <polyline points="480,60 530,60 570,5 665,5" style="fill:none;stroke:#c8cccf;stroke-width:4" />  
            Sorry, your browser does not support inline SVG.
        </svg>
    </div>
</template>

<script>
    export default {
        name: "WheelsSVG",
        props: ['isRightFilled'],
        computed: {
            getRectStyle() {
                const common = 'stroke-width:5;opacity:0.8;';
                return this.isRightFilled === 'true' ? `${common}fill:#ED8138;stroke:#DA7235;` : `${common}fill:#FFFFFF;stroke:#DFE3E6;`
            },
        }
    }
</script>
