
import React, { PropTypes } from 'react';
import Moment from 'moment';
import Select from 'react-select';
//import s from './styles.scss';

import '../styles/index.scss';

//import {Button } from 'react-bootstrap';
import DatePicker from 'react-datepicker';
import DateTime from 'react-datetime';


const API_URL = 'http://spire.ideahack.com'

class MemberFilters extends React.Component {


    constructor(props) {
        super(props);

        this.state = {
            startDate: '',
            endDate: '',
            region: '',
            industry: '',
            membershipLevelFilter: '',
            regionFilter: '',
            industryFilter: '',
            degreeFilter: '',
            membershipLevels: [],
            memberRegions: [],
            memberIndustry: [],
            memberDegree: [],
            joinedStart: '',
            joinedEnd: '',
            gradStart: '',
            gradEnd:'',

        };
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleLevelChange = this.handleLevelChange.bind(this);
        this.handleIndustryChange = this.handleIndustryChange.bind(this);
        this.handleRegionChange = this.handleRegionChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleJoinedStart = this.handleJoinedStart.bind(this);
        this.handleJoinedEnd = this.handleJoinedEnd.bind(this);
        this.handleGradStart = this.handleGradStart.bind(this);
        this.handleGradEnd = this.handleGradEnd.bind(this);
    	this.handleDegreeChange = this.handleDegreeChange.bind(this);
        this.clearFilters = this.clearFilters.bind(this);
}


    componentDidMount() {
        this.getMembershipLevels();
        this.getMemberRegions();
        this.getMemberIndustry();
        this.getMemberDegrees();
    }

    getMemberDegrees(){

    	var degrees = [
    		{
    			'value': 'UNDERGRAD',
	        	'label': 'undergrad',
	    	},
	    	{
    			'value': 'MA',
	        	'label': 'ma',
	    	},
	    	{
    			'value': 'MS',
	        	'label': 'ms',
	    	},
	    	{
    			'value': 'MBA',
	        	'label': 'mba',
	    	},
	    	{
    			'value': 'JD',
	        	'label': 'js',
	    	},
	    	{
    			'value': 'PHD',
	        	'label': 'phd',
	    	},
    	]

    	this.setState({ memberDegree: degrees });
    }


    getMemberRegions(){
        var _this = this;
        fetch(API_URL + '/api/member-regions/')
        .then(response=> response.json())
        .then(function (json) {
            //transform response
            var regions = []
            json.forEach(function (region, index) {
                regions.push({
                    'value': region.region,
                    'label': region.region,
                });
                
            })
            _this.setState({ memberRegions: regions });

        }).catch(function (ex) {
            console.log(ex);
        })
    }


    getMemberIndustry(){
        var _this = this;
        //get membership level option for select box
        fetch(API_URL + '/api/member-industry/')
        .then(response=> response.json())
        .then(function (json) {
            //transform response
             console.log(json)
            var industrys = []
            json.forEach(function (industry, index) {
                industrys.push({
                    'value': industry.industry,
                    'label': industry.industry,
                });
                
            })
            _this.setState({ memberIndustry: industrys });

        }).catch(function (ex) {
            console.log(ex);
        })
    }
    

    getMembershipLevels(){
         var _this = this;
        //get membership level option for select box
        fetch(API_URL + '/api/membership-levels/')
        .then(response=> response.json())
        .then(function (json) {
            //transform response
            var levels = []
            json.forEach(function (level, index) {
                levels.push({
                    'value': level.level,
                    'label': level.level
                });
                
            })
            console.log(levels)
            _this.setState({ membershipLevels: levels });

        }).catch(function (ex) {
            console.log(ex);
        })

    }

    componentWillReceiveProps(nextProps){
        
    }

    clearFilters(){
        this.setState({
            startDate: '',
            endDate: '',
            region: '',
            industry: '',
            membershipLevelFilter: '',
            regionFilter: '',
            industryFilter: '',
            joinedStart: '',
            joinedEnd: '',
            gradStart: '',
            gradEnd:'',
        });
        this.props.onFilter('');
    }

    
    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
    }

    handleLevelChange(val){
        this.setState({membershipLevelFilter: val});
    }

    handleRegionChange(val){
        this.setState({regionFilter: val});
    }

    handleIndustryChange(val){
        this.setState({industryFilter: val});
    }

    handleDegreeChange(val){
        this.setState({degreeFilter: val});
    }

    handleJoinedStart(val){
        this.setState({joinedStart: val});
    }

    handleJoinedEnd(val){
        this.setState({joinedEnd: val});
    }

    handleGradStart(val){
        this.setState({gradStart: val.format('YYYY')});
    }

    handleGradEnd(val){
        this.setState({gradEnd: val.format('YYYY')});
    }

    handleSubmit(event) {
        

        event.preventDefault();
        
        //build query
        var query = '';

        var start = Moment(this.state.joinedStart)
        var end = Moment(this.state.joinedEnd)

        if(start.isValid()){
            query += `&date_joined__gte=${start.format('YYYY-MM-DD')}`;
        }
        if(end.isValid()){
            query += `&date_joined__lte=${end.format('YYYY-MM-DD')}`;
        }
        if(this.state.industryFilter){
            query += `&industry=${this.state.industryFilter}`;
           
        }
        if(this.state.regionFilter){
            query += `&region__in=${this.state.regionFilter}`;
        }
        if(this.state.membershipLevelFilter){
            query += `&membership_level__level=${this.state.membershipLevelFilter}`;
        }

        if(this.state.gradStart){
            query += `&grad_year__gte=${this.state.gradStart}`;
        }
        if(this.state.gradEnd){
            query += `&grad_year__lte=${this.state.gradEnd}`;
        }

          
        this.props.onFilter(query);
    }
   

    render() {
        return (
            <div >   
                <form className="form" onSubmit={this.handleSubmit}>
                    <div className="row">
                        
                    
                        
                        <div className="col-sm-4">
                            <div className="form-group">
                                <label>Region Affiliation</label>
                                <Select
                                    name="regions"
                                    value={this.state.regionFilter}
                                    options={this.state.memberRegions}
                                    onChange={this.handleRegionChange}
                                    multi={true}
                                    simpleValue={true}
                                    
                                />
                            </div>
                        </div>
                        <div className="col-sm-4">
                            <div className="form-group">
                                <label>Industry Sector</label>
                                <Select
                                    name="industry"
                                    value={this.state.industryFilter}
                                    options={this.state.memberIndustry}
                                    onChange={this.handleIndustryChange}
                                    multi={false}
                                    simpleValue={true}
                                   
                                />
                            </div>
                        </div>

                         <div className="col-sm-4">
                            <div className="form-group">
                                <label>Degree</label>
                                <Select
                                    name="industry"
                                    value={this.state.degreeFilter}
                                    options={this.state.memberDegree}
                                    onChange={this.handleDegreeChange}
                                    multi={true}
                                    simpleValue={true}
                                   
                                />
                            </div>
                        </div>
                        
                        <div className="col-sm-12">
                            <button className="btn btn-primary" type="submit" >Filter</button>
                            <button className="btn btn default pull-right" type="button" onClick={this.clearFilters} >Clear</button>
                        </div>                          
                    </div>
                </form>
            </div>
        );
    }

}

export default MemberFilters;
