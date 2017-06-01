import React from 'react';

import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table';

import '../styles/index.scss';

import MemberFilters from './filters'
import Moment from 'moment';
import DebounceInput from 'react-debounce-input';
import { Collapse, Well, Button, Panel } from 'react-bootstrap';

const API_URL = 'http://spire.ideahack.com'

export default class App extends React.Component {



  	constructor(props) {
    super(props);


    	this.state = {
	      members: [],
	      membershipLevels: {},
	      page: 1,
	      sizePerPage: 50,
	      totalSize: 0,
	      startDate: '',
	      endDate: '',
	      filtersOpen: false,
	      searchString: '',
	      progress: false,
	      filters: '',
	      sortName: 'email',
	      sortOrder: 'desc'
	    };


	    this.fetchData = this.fetchMembers.bind(this);
	    this.handleSubmit = this.handleSubmit.bind(this);
	    this.handlePageChange = this.handlePageChange.bind(this);

	    this.onSizePerPageList = this.onSizePerPageList.bind(this);

	    this.handleRowSelect = this.handleRowSelect.bind(this);
	    this.onRowClick = this.onRowClick.bind(this);
	    this.onExportToCSV = this.onExportToCSV.bind(this);
	    this.onSearchChange = this.onSearchChange.bind(this);
	    this.onSortChange = this.onSortChange.bind(this);
	    this.handleSelectAll = this.handleSelectAll.bind(this);
	    
	    this.regionFormatter = this.regionFormatter.bind(this);
	    this.addressFormatter = this.addressFormatter.bind(this);
	    this.companyFormatter = this.companyFormatter.bind(this);
		this.titleFormatter = this.titleFormatter.bind(this);

	    this.industryFormatter = this.industryFormatter.bind(this);

	    this.imageFormatter = this.imageFormatter.bind(this);

	    this.filterMembers = this.filterMembers.bind(this);
	    this.clearSearchFilter = this.clearSearchFilter.bind(this);
	    this.getExportFileName = this.getExportFileName.bind(this);
	}

	fetchMembers(page = this.state.page, sizePerPage = this.state.sizePerPage) {
    var _this = this;
	    //this.setState({progress: true});

	    //get memmbers

	    fetch(API_URL + `/api/members/?page=${page}&page_size=${sizePerPage}`)
	      .then(function (response) {
	        return response.json();
	      })
	      .then(function (json) {
	        _this.setState({ members: json.results, totalSize: json.count, progress: false });

	      }).catch(function (e) {
	        console.log(e);
	      });
	  }
	

	componentDidMount() {
		this.fetchMembers();
	}



  searchMembers(search) {
    var _this = this;
    this.setState({progress: true});
    
    fetch(API_URL + `/api/members/?search=${search}`)
      .then(function (response) {
        return response.json();
      })
      .then(function (json) {
        
        _this.setState({ members: json.results, progress: false });
      }).catch(function (e) {
        console.log('parsing failed', e)
      })
  }


  filterMembers(query, page = 1, sizePerPage = this.state.sizePerPage) {
    var _this = this;
    

    this.setState({progress: true, page: page, filters: query});// set back to first page to avoid invalid page

    fetch(API_URL + `/api/members/?page=${page}&page_size=${sizePerPage}${query}`)
      .then(function (response) {
        return response.json();
      })
      .then(function (json) {
        _this.setState({ members: json.results, totalSize: json.count, progress:false });

      }).catch(function (e) {
        console.log(e);
      });
  }

  
  sortMembers(page = this.state.page, sizePerPage = this.state.sizePerPage, sortName = this.state.sortName, sortOrder = this.state.sortOrder, filter = this.state.filters){
    var _this = this;
    //console.log(sortName);
    //console.log(sortOrder);
    var sort = '';
    if(sortOrder == 'desc'){
      sort = '-';
    }else{
      sort = '';
    }

    //add user__ to sort on foreign key (limitation of django rest framework) will need to come up with a solution
    fetch(API_URL + `/api/members/?page=${page}&page_size=${sizePerPage}&ordering=${sort}user__${sortName}`)
      .then(function (response) {
        return response.json();
      })
      .then(function (json) {
        _this.setState({ members: json.results, totalSize: json.count, progress:false });

      }).catch(function (e) {
        console.log(e);
      });
  }

	priceFormatter(cell, row){
		  return '<i class="glyphicon glyphicon-usd"></i> ' + cell;
	}

	dateFormatter(cell, row) {
    return Moment(cell).format('MMMM Do YYYY');
  }

  addressFormatter(cell,row){
    if(cell){
      return cell.city + ', ' + cell.state;
    }
    return cell
  }

  titleFormatter(cell,row){
    if(cell){
      return cell.title;
    }
    return cell
  }


  imageFormatter(cell,row){
  	return `<img src="${cell}" width="80" class="user-image">`;
  }


  companyFormatter(cell,row){
    if(cell){
      return cell.company;
    }
    return cell
  }

  industryFormatter(cell,row){
    if(cell){
      return cell.industry;
    }
    return cell
  }


  regionFormatter(cell, row) {
    return cell.map(function (elem) {
      return elem.region;
    }).join(",");
  }

  handleRowSelect(row, isSelected, e) {
    if (isSelected) {
      this.selected.push(row);
    } else {
      //find the selected row and remove from selected array
      for (var i = 0; i < this.selected.length; i++) {
        if (this.selected[i].id == row.id) {
          return this.selected.splice(i, 1);
        }
      }
    }
  }

  getExportFileName(){
    return `member-export-${Moment(new Date()).format('YYYY-MM-DD_HH:MM')}.csv`;
  }

  handleSelectAll(isSelected, rows) {
    if (isSelected) {
      this.selected = rows;
    } else {
      this.selected = [];
    }
  }

   handleSubmit(event) {
    event.preventDefault();
   }

  onRowClick(row) {
    history.push({ pathname: Config.baseUrl + `/members/${row.id}`, state: row.id });
  }

  onExportToCSV(row) {
    return this.selected;
  }


  buttonFormatter(cell, row) {
    return '<span class="fa fa-pencil"></span>';
  }


  handlePageChange(page, sizePerPage) {
    this.setState({page: page})
    this.fetchMembers(page, sizePerPage);
  }

  onSizePerPageList(sizePerPage){
    // When changing the size per page always navigating to the first page
    this.setState({sizePerPage: sizePerPage});
    this.fetchMembers(1, sizePerPage); 
  }

  onSearchChange(event) {
    this.setState({ searchString: event.target.value })
    this.searchMembers(this.state.searchString);
  }

  onSortChange(sortName, sortOrder){
    
    this.setState({
      sortName: sortName,
      sortOrder: sortOrder
    });
   
    this.sortMembers();
  }

  clearSearchFilter() {
    this.setState({ searchString: '' });
    this.fetchMembers(1, this.state.sizePerPage);
  }

  handleStartDateChange(event) {
    this.setState({ startDate: event.target.value });
  }

  handleEndDateChange(event) {
    this.setState({ endDate: event.target.value });
  }


  render() {

  	const selectRow = {
      mode: 'checkbox',
      onSelect: this.handleRowSelect,
      onSelectAll: this.handleSelectAll
    };
    const options = {
      //defaultSearch: 'first_name'
      onRowClick: this.onRowClick,
     
      //paging
      sizePerPage: this.state.sizePerPage,
      paginationSize: 5,
      page: this.state.page,

      sizePerPageList: [{
        text: '50', value: 50
      }, {
        text: '100', value: 100
      }, {
        text: '200', value: 200
      }, {
        text: 'All', value: this.state.totalSize
      }],

      onPageChange: this.handlePageChange,
      onSizePerPageList: this.onSizePerPageList,
      paginationShowsTotal: false,

      //searching
      onSearchChange: this.onSearchChange,
      clearSearch: true,

      //sorting
      sortName: this.state.sortName,
      sortOrder: this.state.sortOrder,
      onSortChange: this.onSortChange,

    };


    return (
      <div>

      	<div className="row search-row">
          <form className="form" onSubmit={this.handleSubmit}>
            <div className="col-sm-12">
              <div className="input-group">
             
                  <DebounceInput
                    placeholder="Search by keyword..."
                    value={this.state.searchString}
                    type="text"
                    className="form-control"
                    minLength={2}
                    debounceTimeout={300}
                    onChange={this.onSearchChange} />

                <span className="input-group-btn">
                  <button className="btn btn-default" type="button" onClick={this.clearSearchFilter}>Clear</button>
                </span>
              </div>
            </div>
          </form>
        </div> 

        <div className="row filter-row">
          <div className="col-sm-12">
            <Button onClick={() => this.setState({ filtersOpen: !this.state.filtersOpen })} block className="collapse-button">
             Advanced Search Filters<span className={`fa ${this.state.filtersOpen ? 'fa-caret-down' : 'fa-caret-up'}`}></span>
            </Button>
            <Collapse in={this.state.filtersOpen}>
              <div>
                <Well>
                  <MemberFilters onFilter={this.filterMembers}></MemberFilters>
                </Well>
              </div>
            </Collapse>
          </div>
        </div>

         <BootstrapTable fetchInfo={{ dataTotalSize: this.state.totalSize }} remote data={this.state.members} pagination options={options} bordered={false}>
          <TableHeaderColumn isKey hidden dataField='id'>ID</TableHeaderColumn>

          <TableHeaderColumn dataField='image' dataFormat={this.imageFormatter}></TableHeaderColumn>
          <TableHeaderColumn dataField="first_name" dataSort={true}>First Name</TableHeaderColumn>
          <TableHeaderColumn dataField="last_name" dataSort={true}>Last Name</TableHeaderColumn>
          <TableHeaderColumn dataField="address" dataFormat={this.addressFormatter}>Location</TableHeaderColumn>

          <TableHeaderColumn dataField="professional_information" dataFormat={this.titleFormatter}>Title</TableHeaderColumn>
          
          <TableHeaderColumn dataField="professional_information" dataFormat={this.companyFormatter}>Company</TableHeaderColumn>
          <TableHeaderColumn dataField="degree_string">Degree</TableHeaderColumn>
        </BootstrapTable>

      </div>
    )
  }
}
