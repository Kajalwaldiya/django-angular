import { Component } from '@angular/core';
import {Http, Response} from '@angular/http';
import { HttpClient} from '@angular/common/http';
import {map} from 'rxjs/operators';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'myAngularProject';
  // httpOptions = {
  //   headers: new Headers({
  //     'Accept': 'text/csv, */*',
  //     // 'Authorization': 'my-auth-token',
  //     'Access-Control-Allow-Origin': '*',
  //     'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
  //     'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With'
  //   })
  // };
  private apiUrl = 'http://localhost:8000/apiview/';
  data: any = [];
  name: string;
  date: any;
  address: string;
  department: string;

  constructor(private http: Http, private httpClient: HttpClient) {
    this.personalDetails();
    this.displayAPI();
  }

  personalDetails() {
    return this.http.get(this.apiUrl)
      .pipe(map((res: Response) => res.json()));
  }

  displayAPI() {
    this.personalDetails().subscribe(data => {
      this.data = data;
      // console.log(data);
    });
  }

  someFunction(user) {
    this.httpClient.post(this.apiUrl,
      {
        name:user.name,
        age: user.date,
        email:user.address,
        phone:user.department,
      })
      .subscribe(
        (data:any) => {
          console.log(data);
        }
      )
      location.reload();
  }
}
