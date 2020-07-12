import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api/api.service';
import { Router } from '@angular/router';
import { FamilyFilterPipe } from '../pipe/family-filter.pipe';

@Component({
  selector: 'app-family-control',
  templateUrl: './family-control.component.html',
  styleUrls: ['./family-control.component.css'],
})
export class FamilyControlComponent implements OnInit {
  members = [];
  correspondingOwner: any;
  pattern : string;
  constructor(private api: ApiService,private router : Router,private pipe : FamilyFilterPipe) {}
  ngOnInit(): void {
    this.api.getFamilyMembers().subscribe(
      (data) => {
        this.members = data;
        this.getCorrespondingOwner();
      },
      (error) => {
        console.log(error);
      }
    );
  }

  getCorrespondingOwner(): void {
    this.members.forEach((element) => {
      this.api.getOwner(element.owner).subscribe(
        (data) => {
          this.correspondingOwner = data;
          console.log(this.correspondingOwner);
        },
        (error) => {
          console.log(error);
        }
      );
    });
  }

  // Refresh the page
  onInit(): void {
    this.api.getFamilyMembers().subscribe(
      (data) => {
        this.members = data;
      },
      (error) => {
        console.log(error);
      }
    );
  }

  deleteMember(oid): void {
    this.api.deleteMember(oid).subscribe(
      (data) => {
        this.members.push(data);
        this.onInit();
      },
      (error) => {
        console.log(error);
        this.onInit();
      }
    );
  }
  searchFamily(pattern): void {
    console.log(pattern);
    if (pattern) {
      this.members = this.pipe.transform(this.members, pattern);
    } else {
      this.onInit();
    }
  }

  logOut(){
    localStorage.removeItem('userToken');
    this.router.navigate(['login']);
  }
}
