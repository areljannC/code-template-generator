REACT = '''
import React from 'react'

/* Component */
const Component = () => {
    return <div>Hello</div>
}

export default Component
'''

REACT_REDUX = '''
import React from 'react'
import { connect } from 'react-redux'

/* Redux Mappings */
const mapStateToProps = state => ({})
const mapDispatchToProps = dispatch => ({})

/* Component */
const Component = ({}) => {
    return <div>Hello</div>
}

export default connect(mapStateToProps, mapDispatchToProps)(Component)
'''

REACT_STYLED_COMPONENTS = '''
import React from 'react'
import styled from 'styled-components'

/* Component */
const Component = () => {
    return (
        <ComponentContainer>
            Hello
        </ComponentContainer>
    )
}

/* Styles */
const ComponentContainer = styled.div``

export default Component
'''

REACT_PROP_TYPES = '''
import React from 'react'
import PropTypes from 'prop-types'

/* Component */
const Component = ({ stringProp = 'default string' }) => {
    return <div>{stringProp}</div>
}

/* Prop Types */
Component.propTypes = {
    stringProp: PropTypes.string
}

export default Component
'''

REACT_ALL = '''
import React from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import styled from 'styled-components'

/* Redux Mappings */
const mapStateToProps = state => ({})
const mapDispatchToProps = dispatch => ({})

/* Component */
const Component = ({ stringProp = 'default string' }) => {
    return (
        <ComponentContainer>
            stringProp
        </ComponentContainer>
    )
}

/* Prop Types */
Component.propTypes = {
    stringProp: PropTypes.string
}

/* Styles */
const ComponentContainer = styled.div``

export default connect(mapStateToProps, mapDispatchToProps)(Component)
'''