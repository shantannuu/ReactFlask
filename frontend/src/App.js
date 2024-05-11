import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
    const [name, setName] = useState('');
    const[data,setData] = useState([]);
    const[edit,setEdit] = useState(false);
    const[id , setId] = useState(0);
    
    const handleDelete = async (id) => {
      try {
        await axios.delete(`http://localhost:5000/api/delete-data/${id}`);
        getData()
      } catch (error) {
        alert('Error deleting data');
        console.error(error);
      }
    }
    
    const handleSubmit = async (e) => {
      e.preventDefault();
      if(edit === true){
        try {
          await axios.put(`http://localhost:5000/api/update-data/${ id }`, { name });
          setName('');
          setId(0);
          setEdit(false)
          getData();
        } catch (error) {
          alert('Error posting data');
          console.error(error);
        }
      }else{
        try {
          await axios.post('http://localhost:5000/api/post-data', { name });
          setName('');
          getData();
        } catch (error) {
          alert('Error posting data');
          console.error(error);
        }
      }
      
    };

    useEffect(()=>{
      getData();
    },[])

    const getData = async () =>{
      try {
        const response = await axios.get('http://localhost:5000/api/get-data');
        setData(response.data);
      } catch (error) {
        alert('Error getting data');
        console.error(error);
      }
    }

    const handleEdit = (id,name) =>{
      setEdit(true);
      setName(name);
      setId(id);
    }
   
    return (
      <div>
      <h2>Data</h2>
      <h2>Post Data</h2>
      { data.map((item) =>(
        <>
          <h2>Name : { item.name }</h2>
          <button onClick={() => handleEdit(item.id ,item.name)}>Edit</button>    
          <button onClick={() => handleDelete(item.id)}>Delete</button>
          </>
      ) )}
      <form  onSubmit={handleSubmit}>

        { edit === true ? (
          <>
          <label>
            New Name:
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
          </label>
          <button  type="submit">edit</button>
          </>
          ) : (<>
            <label>
              Name:
              <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <button  type="submit">Submit</button>
            </>)
        }
      </form>
    </div>
    );
};


export default App;